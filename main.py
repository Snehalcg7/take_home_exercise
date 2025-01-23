# • https://catalog.redhat.com/api/containers/docs/
# • https://catalog.redhat.com/api/containers/v1/ui/

# rhbk/keycloak-rhel9.
import requests

#define required variables
repo_name = "rhbk/keycloak-rhel9"
registory_name = "registry.access.redhat.com"
respose_data = []

# Get Images data from repository
get_reg_url = f"https://catalog.redhat.com/api/containers/v1/repositories/registry/{registory_name}/repository/{repo_name}"
registory_data_response = requests.get(get_reg_url)
data = registory_data_response.json()
content_stream_grades = data.get('content_stream_grades')

for each_cotent_stream in content_stream_grades:
    content_strem = {}
    content_strem["content_strem"] = each_cotent_stream.get('tag')
    images_id_list = []    
    for image_id in each_cotent_stream.get("image_ids"):
        images_id_list.append(image_id.get('id'))
    print(images_id_list)
  #  publisted_date, vcsRef, grade = get_latest_images(images_id_list)
   

print(respose_data)