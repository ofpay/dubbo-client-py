#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gzip

from dubbo.common.compression.compression import Compression


class GzipCompression(Compression):
    """Gzip compression implementation."""

    def compress(self, data: bytes) -> bytes:
        """
        Compress data using gzip.
        :param data: data to be compressed.
        :return: compressed data.
        """
        return gzip.compress(data)

    def decompress(self, data: bytes) -> bytes:
        """
        Decompress data using gzip.
        :param data: data to be decompressed.
        :return: decompressed data.
        """
        return gzip.decompress(data)
