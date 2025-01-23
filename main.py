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

# Get image required fields 
get_images_url = requests.get(f"{get_reg_url}/images")
images_data = get_images_url.json()
for images in images_data.get('data'):
    last_updated_date = images.get("last_update_date")
  #  respose_data["last_update_date"] = last_updated_date
    for labels in images.get("parsed_data").get("labels"):
        if labels.get('name') == "vcs-ref":
            vcs_ref = labels.get('value')
   #         respose_data["vcs_ref"] = vcs_ref

print(respose_data)