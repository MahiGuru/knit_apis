from rest_framework import serializers
from products.p_models.category_model import Category
from .image_serializer import ImageSerializer
class CategorySerializer(serializers.ModelSerializer):
    images_list = serializers.SerializerMethodField(read_only=True)
    
    def get_images_list(self, obj):
        serializer = ImageSerializer(obj.images, many=False)
        return serializer.data 

    class Meta:
        model = Category
        fields = ('id', 'name', 'code', 'description', 'images_list')

    def validate(self, data):
        if data.get('name'):
            data['code'] = data.get('name', '').replace(" ", "_").upper()
        else:
            raise serializers.ValidationError("Category name is required")
        
        hasCategory = Category.objects.filter(code=data['code'])
        if(len(hasCategory)):
            raise serializers.ValidationError("Category already existed")
        return data

    def create(self, validated_data):
        validated_data['code'] = validated_data.get('code')
        validated_data['description'] = self.initial_data.get('description', None)
        try:
            category = Category.objects.get(code=validated_data.get('code'))
            category.name = validated_data.get('name', category.name)
            category.description = validated_data.get('description', category.description)
            category.code =  validated_data.get('code', category.code).upper()
            category.save()
        except Category.DoesNotExist:
            category = Category(**validated_data)
            category.save()
        return category

    def update(self, instance, validated_data):
        # Update the Foo instance
        instance.title = validated_data.get('name', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.code =  validated_data.get('code', instance.code).upper()   
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
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='category_'+str(instance.id), size=c_image.size)
                instance.images.add(images)

        return instance



























