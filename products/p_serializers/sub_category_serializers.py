
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from .image_serializer import ImageSerializer
from .category_serializers import CategorySerializer

from ..p_models.image_model import PImage
from ..p_models.category_model import Category
from ..p_models.sub_category_model import SubCategory

import logging
logger = logging.getLogger(__name__)

class SubCategorySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True, allow_null=True)
    categoryId = serializers.ReadOnlyField(source='category.id')
    category = serializers.ReadOnlyField(source='category.name')

    errors = {}

    def get_images(self, obj):
        serializer = KImageSerializer(obj.images, many=True)
        return serializer.data 
    
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'code', 'description','categoryId', 'category',  'images')

    def validate(self, data):
        self.errors = {}
        if self.initial_data.get('name'):
            data['code'] = self.initial_data.get('name', '').replace(" ", "_").upper()
        else:
            self.errors['name'] = 'Category name required' 
        
        hasSubCategory = SubCategory.objects.filter(code= data['code'])
        if len(hasSubCategory):
            self.errors['subcategory_exists'] = 'Sub Category already exists' 

        if self.initial_data.get('category') is None:
            self.errors['category'] = 'Category type required'
        if len(self.errors):
            logger.info(self.errors)
            raise serializers.ValidationError(self.errors)
        return data

    def create(self, validated_data):
        ## Image data
        validated_data['code'] = validated_data['code'].upper() if validated_data['code'] else None
        validated_data['description'] = self.initial_data.get("description")
        if self.initial_data.get('category'):
            categoryQuerySet = Category.objects.filter(id= int(self.initial_data['category']))
            category = serializers.PrimaryKeyRelatedField(queryset=categoryQuerySet, many=False)
            if len(categoryQuerySet):
                validated_data['category'] = categoryQuerySet[0]
        
        try:
            subCategory = SubCategory.objects.get(code=validated_data.get("code"))
            subCategory.name = validated_data.get('name', subCategory.name)
            subCategory.category = validated_data.get('category', subCategory.category)
            subCategory.description = validated_data.get('description', subCategory.description)
            subCategory.code =  validated_data.get('code', subCategory.code).upper()
            if self.initial_data.get("images"):
                for e in subCategory.images.all():
                    subCategory.images.remove(e)
                    KImage.objects.get(id=e.id).delete()
            subCategory.save()
        except SubCategory.DoesNotExist:
            subCategory = SubCategory(**validated_data)
            subCategory.save()
        
        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='subcategorys/subcat_'+str(subCategory.id), size=c_image.size)
                subCategory.images.add(images)         

        return subCategory

    def update(self, instance, validated_data):
        # Update the Foo instance
        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.code =  validated_data.get('code', instance.code).upper()   
        
        if self.initial_data['category']:
            categoryQuerySet = Stitch.objects.filter(id= int(self.initial_data['category']))
            instance.category = categoryQuerySet[0] if len(categoryQuerySet) else None        
        instance.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')

            ### Remove relational images if any ####
            for e in instance.images.all():
                instance.images.remove(e)
                KImage.objects.get(id=e.id).delete()
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='subCategory_'+str(instance.id), size=c_image.size)
                instance.images.add(images)

        return instance