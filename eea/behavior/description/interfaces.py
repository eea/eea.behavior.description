"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.autoform.interfaces import IFormFieldProvider

from plone.supermodel import model
from zope.interface import provider
from zope.schema import TextLine
from eea.behavior.description import EEAMessageFactory as _


class IEeaBehaviorDescriptionLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


@provider(IFormFieldProvider)
class IDescriptionMetadata(model.Schema):
    """Description metadata schema provider"""

    #
    # Metadata
    #
    model.fieldset(
        "metadata",
        label=_("Metadata"),
        fields=[
            "description_metadata_blocks",
        ],
    )

    description_metadata_blocks = TextLine(
        title=_("Description"),
        description=_(
            "This property extracts description metadata from Volto blocks in current page."
        ),
        required=False,
        default="",
    )
