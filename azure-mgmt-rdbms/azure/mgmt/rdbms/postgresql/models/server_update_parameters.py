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


class ServerUpdateParameters(Model):
    """Parameters allowd to update for a server.

    :param sku: The SKU (pricing tier) of the server.
    :type sku: :class:`Sku <azure.mgmt.rdbms.postgresql.models.Sku>`
    :param storage_mb: The max storage allowed for a server.
    :type storage_mb: long
    :param administrator_login_password: The password of the administrator
     login.
    :type administrator_login_password: str
    :param version: The version of a server. Possible values include: '9.5',
     '9.6'
    :type version: str or :class:`ServerVersion
     <azure.mgmt.rdbms.postgresql.models.ServerVersion>`
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or :class:`SslEnforcementEnum
     <azure.mgmt.rdbms.postgresql.models.SslEnforcementEnum>`
    :param tags: Application-specific metadata in the form of key-value pairs.
    :type tags: dict
    """

    _validation = {
        'storage_mb': {'minimum': 1024},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'storage_mb': {'key': 'properties.storageMB', 'type': 'long'},
        'administrator_login_password': {'key': 'properties.administratorLoginPassword', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'ssl_enforcement': {'key': 'properties.sslEnforcement', 'type': 'SslEnforcementEnum'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, sku=None, storage_mb=None, administrator_login_password=None, version=None, ssl_enforcement=None, tags=None):
        self.sku = sku
        self.storage_mb = storage_mb
        self.administrator_login_password = administrator_login_password
        self.version = version
        self.ssl_enforcement = ssl_enforcement
        self.tags = tags