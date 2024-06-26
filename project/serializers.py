from rest_framework import serializers

from gallery import serializers as gallery_serial

from project import models


class SpecificationsSerializer(serializers.ModelSerializer):
    """Specifications Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Project_Specification
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    """Property Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Project_Property
        fields = "__all__"


class ProjectListSerializer(serializers.ModelSerializer):
    """Project List Serializer"""

    class Meta:
        model = models.Project
        fields = ["id", "title", "image"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["url"] = instance.image.url

        return rep


class FeatureSerializer(serializers.ModelSerializer):
    """Feature Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.Feature
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)

    #     rep["url"] = instance.logo.url

    #     return rep


class BlockSpecificationSerializer(serializers.ModelSerializer):
    """BlockSpecification Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Block_Specification
        fields = "__all__"


class BlockListSerializer(serializers.ModelSerializer):
    """Block List Serializer"""

    specs = BlockSpecificationSerializer(many=True)

    class Meta:
        model = models.Block
        fields = ["id", "title", "specs"]


class ProjectSerializer(serializers.ModelSerializer):
    """Project Serializer"""

    gallery = gallery_serial.GallerySerializer(many=True)
    media = gallery_serial.MediaSerializer(many=True)
    features = FeatureSerializer(many=True)
    specs = SpecificationsSerializer(many=True)
    props = PropertySerializer(many=True)
    blocks = BlockListSerializer(many=True)

    class Meta:
        """Meta Class"""

        model = models.Project
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     relational_products = (
    #         models.Product.objects.get_relational_products_by_category(
    #             instance.category.id
    #         )
    #     )
    #     if len(relational_products):
    #         rep["relational_products"] = relational_products
    #     else:
    #         rep["relational_products"] = []
    #     return rep
