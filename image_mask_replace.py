#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[summary]
  マスク画像置き換え
[description]
  -
"""

import os
import copy
import argparse
import glob

import numpy as np
import cv2 as cv


def get_args():
    """
    [summary]
        引数解析
    Parameters
    ----------
    None
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--width", help='capture width', type=int)
    parser.add_argument("--height", help='capture height', type=int)
    parser.add_argument(
        "--original", help='save original file', type=bool, default=False)
    args = parser.parse_args()

    return args


def resize_function(width, height):
    """
    [summary]
        画像リサイズ用関数生成
    Parameters
    ----------
    width : [int]
        [description]
            リサイズ幅
    height : [int]
        [description]
            リサイズ高さ
    """

    def resize(image):
        if (width is not None) and (height is not None):
            resize_image = cv.resize(image, (width, height))
        else:
            resize_image = copy.deepcopy(image)
        return resize_image

    return resize


def main():
    """
    [summary]
        main()
    Parameters
    ----------
    None
    """
    # 引数解析 #################################################################
    args = get_args()
    width = args.width
    height = args.height
    is_save_original = args.original

    # 各ディレクトリパス準備 ####################################################
    path_image = os.path.join('image', 'image')
    path_mask = os.path.join('image', 'mask')
    path_replace = os.path.join('image', 'replace')
    path_output = os.path.join('image', 'output')

    # ファイルリスト取得 ########################################################
    image_files = glob.glob(os.path.join(path_image, '*'))
    mask_files = glob.glob(os.path.join(path_mask, '*'))
    replace_files = glob.glob(os.path.join(path_replace, '*'))

    # リサイズ用関数生成 ########################################################
    sample_image = cv.imread(image_files[0])
    if width is None:
        width = sample_image.shape[1]
    if height is None:
        height = sample_image.shape[0]
    image_resize = resize_function(width, height)

    for image_file, mask_file in zip(image_files, mask_files):
        # 画像/マスク画像取得 ###################################################
        image_filename = os.path.splitext(os.path.basename(image_file))[0]
        mask_filename = os.path.splitext(os.path.basename(mask_file))[0]
        if image_filename != mask_filename:
            continue

        image = cv.imread(image_file)
        mask = cv.imread(mask_file, 0)

        # オリジナル画像(リサイズ)保存 ###########################################
        if is_save_original:
            save_filename = os.path.join(
                path_output, image_filename + '_{:03}.jpg'.format(0))
            resize_image = image_resize(image)
            cv.imwrite(save_filename, resize_image)

        # マスク画像を元に画像を合成 #############################################
        for i, replace_file in enumerate(replace_files):
            r_image = cv.imread(replace_file)

            resize_image = image_resize(image)
            resize_mask = image_resize(mask)
            resize_r_image = image_resize(r_image)

            result_image = np.where(
                np.expand_dims(resize_mask == 255, -1), resize_image,
                resize_r_image)

            save_filename = os.path.join(
                path_output, image_filename + '_{:03}.jpg'.format(i + 1))

            cv.imwrite(save_filename, result_image)
            print('save:' + save_filename)


if __name__ == '__main__':
    main()
