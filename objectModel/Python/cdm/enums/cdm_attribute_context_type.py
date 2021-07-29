﻿# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.

from enum import IntEnum


class CdmAttributeContextType(IntEnum):
    ENTITY = 1
    ENTITY_REFERENCE_EXTENDS = 2
    ATTRIBUTE_DEFINITION = 3
    ATTRIBUTE_GROUP = 4
    GENERATED_SET = 5
    GENERATED_ROUND = 6
    ADDED_ATTRIBUTE_NEW_ARTIFACT = 7
    ADDED_ATTRIBUTE_SUPPORTING = 8
    ADDED_ATTRIBUTE_IDENTITY = 9
    ADDED_ATTRIBUTE_SELECTED_TYPE = 10
    ADDED_ATTRIBUTE_EXPANSION_TOTAL = 11
    PASS_THROUGH = 12
    PROJECTION = 13
    SOURCE = 14
    OPERATIONS = 15
    OPERATION_ADD_COUNT_ATTRIBUTE = 16
    OPERATION_ADD_SUPPORTING_ATTRIBUTE = 17
    OPERATION_ADD_TYPE_ATTRIBUTE = 18
    OPERATION_EXCLUDE_ATTRIBUTES = 19
    OPERATION_ARRAY_EXPANSION = 20
    OPERATION_COMBINE_ATTRIBUTES = 21
    OPERATION_RENAME_ATTRIBUTES = 22
    OPERATION_REPLACE_AS_FOREIGN_KEY = 23
    OPERATION_INCLUDE_ATTRIBUTES = 24
    OPERATION_ADD_ATTRIBUTE_GROUP = 25
    OPERATION_ALTER_TRAITS = 26
    OPERATION_ADD_ARTIFACT_ATTRIBUTE = 27
    UNKNOWN = 28
