# • https://catalog.redhat.com/api/containers/docs/
# • https://catalog.redhat.com/api/containers/v1/ui/

# rhbk/keycloak-rhel9.
import requests

# Get Images data from repository
repo_name = "rhbk/keycloak-rhel9"
registory_name = "registry.access.redhat.com"

get_reg_url = f"https://catalog.redhat.com/api/containers/v1/repositories/registry/{registory_name}/repository/{repo_name}"

respose_data = []
registroy_data_reponse = requests.get(get_reg_url)
data = registroy_data_reponse.json()
content_stream_grades = data.get('content_stream_grades')

        
for each_cotent_stream in content_stream_grades:
    content_strem = {}
    content_strem["content_strem"] = each_cotent_stream.get('tag')
    images_id_list = []    
    for image_id in each_cotent_stream.get("image_ids"):
        images_id_list.append(image_id.get('id'))
    
    print(images_id_list)
    print(content_strem)


