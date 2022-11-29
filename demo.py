a = {'title': {'class': 'yes', 'placeholder': 'default'}, 'description': {'class': 'damng', 'placeholder': 'default'}, 
'featured_image': {'class': 'default', 'placeholder': 'default'}}
# b = a.items()
# # print(b)
for k, v in a:
    v['class'] = 'new style'
    v['placeholder'] = 'write something'

# print(b)

