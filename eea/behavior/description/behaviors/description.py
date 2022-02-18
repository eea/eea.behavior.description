""" Custom behavior for Indicator

"""
from eea.behavior.description.interfaces import IDescriptionMetadata
from plone.dexterity.interfaces import IDexterityContent
from zope.component import adapter
from zope.interface import implementer


def getAllBlocks(blocks, flat_blocks):
    """Get a flat list from a tree of blocks"""
    for block in blocks.values():
        sub_blocks = block.get("data", {}).get("blocks", {}) or block.get("blocks", {})
        flat_blocks.append(block)
        if sub_blocks:
            getAllBlocks(sub_blocks, flat_blocks)
    return flat_blocks


@implementer(IDescriptionMetadata)
@adapter(IDexterityContent)
class Description(object):
    """Automatically extract Description metadata from blocks"""

    def __init__(self, context):
        self.__dict__["context"] = context
        self.__dict__["readOnly"] = ["description"]

    def __getattr__(self, name):  # pylint: disable=R1710
        if name not in IDescriptionMetadata:
            raise AttributeError(name)

        if name not in self.__dict__["readOnly"]:
            return getattr(
                self.__dict__.get("context"),
                name,
                IDescriptionMetadata[name].missing_value,
            )

    def __setattr__(self, name, value):
        if name not in IDescriptionMetadata:
            raise AttributeError(name)

        if name not in self.__dict__["readOnly"]:
            setattr(self.context, name, value)

    @property
    def description_metadata_blocks(self):
        """Description metadata from Volto Blocks"""
        res = []
        blocks = getattr(self.context, "blocks", None) or {}
        for block in getAllBlocks(blocks, []):
            if block.get("@type", "") != "slate":
                continue

            description = block.get("plaintext", "") or ""
            res.append(description)
        return res
