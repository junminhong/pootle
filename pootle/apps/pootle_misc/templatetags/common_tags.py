#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Zuza Software Foundation
# Copyright 2013-2104 Evernote Corporation
#
# This file is part of Pootle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from django import template
from django.contrib.auth import get_user_model


register = template.Library()


@register.inclusion_tag('browser/_table.html', takes_context=True)
def display_table(context, table):
    return {
        'table': table,
    }


@register.filter
def endswith(value, arg):
    return value.endswith(arg)


@register.filter
def count(value, arg):
    return value.count(arg)


@register.filter
def label_tag(field, suffix=None):
    """Returns the `label_tag` for a field.

    Optionally allows overriding the default `label_suffix` for the form
    this field belongs to.
    """
    if not hasattr(field, 'label_tag'):
        return ''

    return field.label_tag(label_suffix=suffix)


@register.inclusion_tag('core/_top_scorers.html')
def top_scorers(*args, **kwargs):
    User = get_user_model()
    allowed_kwargs = ('days', 'language', 'project', 'limit')
    lookup_kwargs = dict(
        (k, v) for (k, v) in kwargs.iteritems() if k in allowed_kwargs
    )

    return {
        'top_scorers': User.top_scorers(**lookup_kwargs),
    }
