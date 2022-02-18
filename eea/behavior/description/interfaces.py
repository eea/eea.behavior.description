"""Module where all interfaces, events and exceptions live."""
# pylint: disable=line-too-long

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import provider
from zope.schema import TextLine

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model


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
            "description_blocks",
        ],
    )

    description_blocks = TextLine(
        title=_("Description"),
        description=_(
            "This property extracts description as metadata"
            "from Volto blocks in current page."
        ),
        required=False,
    )
