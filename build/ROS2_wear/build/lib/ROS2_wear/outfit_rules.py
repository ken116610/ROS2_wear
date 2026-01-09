#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

def suggest_outfit(temp_c: float) -> str:
    if temp_c < 5.0:
        return "厚手コート / 手袋 / マフラー"
    if temp_c < 12.0:
        return "コート / ニット / 長ズボン"
    if temp_c < 18.0:
        return "ジャケット/ 長袖 / 長ズボン"
    if temp_c < 24.0:
        return "薄手の上着 / 長袖 or 半袖"
    if temp_c < 28.0:
        return "半袖 / 薄手パンツ"
    return "半袖 / 帽子 / 飲み物"
