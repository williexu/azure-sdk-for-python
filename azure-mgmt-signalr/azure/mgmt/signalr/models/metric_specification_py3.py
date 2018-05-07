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


class MetricSpecification(Model):
    """Specifications of the Metrics for Azure Monitoring.

    :param name: Name of the metric.
    :type name: str
    :param display_name: Localized friendly display name of the metric.
    :type display_name: str
    :param display_description: Localized friendly description of the metric.
    :type display_description: str
    :param unit: The unit that makes sense for the metric.
    :type unit: str
    :param aggregation_type: Only provide one value for this field. Valid
     values: Average, Minimum, Maximum, Total, Count.
    :type aggregation_type: str
    :param fill_gap_with_zero: Optional. If set to true, then zero will be
     returned for time duration where no metric is emitted/published.
     Ex. a metric that returns the number of times a particular error code was
     emitted. The error code may not appear
     often, instead of the RP publishing 0, Shoebox can auto fill in 0s for
     time periods where nothing was emitted.
    :type fill_gap_with_zero: str
    :param category: The name of the metric category that the metric belongs
     to. A metric can only belong to a single category.
    :type category: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'display_description': {'key': 'displayDescription', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'aggregation_type': {'key': 'aggregationType', 'type': 'str'},
        'fill_gap_with_zero': {'key': 'fillGapWithZero', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, display_name: str=None, display_description: str=None, unit: str=None, aggregation_type: str=None, fill_gap_with_zero: str=None, category: str=None, **kwargs) -> None:
        super(MetricSpecification, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.display_description = display_description
        self.unit = unit
        self.aggregation_type = aggregation_type
        self.fill_gap_with_zero = fill_gap_with_zero
        self.category = category