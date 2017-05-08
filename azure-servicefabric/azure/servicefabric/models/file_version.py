# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FileVersion(Model):
    """Information about the version of image store file.

    :param version_number: The current iamge store version number for the
     file is used in image store for checking whether it need to be updated.
    :type version_number: str
    :param epoch_data_loss_number: The epoch data loss number of image store
     file is used to indicate the status of data loss.
    :type epoch_data_loss_number: str
    """ 

    _attribute_map = {
        'version_number': {'key': 'VersionNumber', 'type': 'str'},
        'epoch_data_loss_number': {'key': 'EpochDataLossNumber', 'type': 'str'},
    }

    def __init__(self, version_number=None, epoch_data_loss_number=None):
        self.version_number = version_number
        self.epoch_data_loss_number = epoch_data_loss_number