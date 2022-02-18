"""Module where all interfaces, events and exceptions live."""
# pylint: disable=line-too-long

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import provider
from zope.schema import Text

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model


from eea.behavior.description import EEAMessageFactory as _


class IEeaBehaviorDescriptionLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


@provider(IFormFieldProvider)
class IDescriptionMetadata(model.Schema):
    """Description metadata schema provider"""

    description = Text(
        title=_("Description (read-only)"),
        description=_(
            "This property is read-only and it is automatically"
            "extracted from the first paragraphs of this document."
        ),
        required=False,
    )
