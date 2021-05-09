from rest_framework import serializers
from products.p_models.brand_model import Brand
from products.p_models.image_model import PImage

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'code', 'description')

    def validate(self, data):
        if data.get('name'):
            data['code'] = data.get('name', '').replace(" ", "_").upper()
        else:
            raise serializers.ValidationError("Brand name is required")
        
        hasBrand = Brand.objects.filter(code=data['code'])
        if(len(hasBrand)):
            raise serializers.ValidationError("Brand already existed")
        return data

    def create(self, validated_data):
        validated_data['code'] = validated_data.get('code')
        validated_data['description'] = self.initial_data.get('description', None)
        try:
            brand = Brand.objects.get(code=validated_data.get('code'))
            brand.name = validated_data.get('name', brand.name)
            brand.description = validated_data.get('description', brand.description)
            brand.code =  validated_data.get('code', brand.code).upper()
            brand.save()
        except Brand.DoesNotExist:
            brand = Brand(**validated_data)
            brand.save()
        return brand

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
                PImage.objects.get(id=e.id).delete()
            for image in image_data:
                c_image= image_data[image]
                images = PImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='Brand_'+str(instance.id), size=c_image.size)
                instance.images.add(images)

        return instance



























