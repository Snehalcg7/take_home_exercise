# • https://catalog.redhat.com/api/containers/docs/
# • https://catalog.redhat.com/api/containers/v1/ui/

# rhbk/keycloak-rhel9.
import requests
import pprint

#define required variables
repo_name = "rhbk/keycloak-rhel9"
registory_name = "registry.access.redhat.com"
respose_data = []

# Get Images data from repository
get_reg_url = f"https://catalog.redhat.com/api/containers/v1/repositories/registry/{registory_name}/repository/{repo_name}"
registory_data_response = requests.get(get_reg_url)
data = registory_data_response.json()
content_stream_grades = data.get('content_stream_grades')

#Get the latest image from each content stream
def get_latest_images(images_list):
    vcs_ref = ""
    flag = 0
   
    for image_id in images_list:
        image_data = requests.get(url=f"https://catalog.redhat.com/api/containers/v1/images/id/{image_id}?include=last_update_date&include=_id&include=parsed_data.labels").json()
        if flag == 0:
            latest_date = image_data.get("last_update_date")
            flag = 1
        elif latest_date is None or image_data.get("last_update_date") > latest_date:
            latest_date = image_data.get("last_update_date")
            for lables in image_data["parsed_data"].get('labels'):
                 if lables.get('name') == "vcs-ref":
                     vcs_ref = lables.get('value')
    return vcs_ref
        
#Get content streams data
for each_cotent_stream in content_stream_grades:
    content_strem = {}
    content_strem["content_strem"] = each_cotent_stream.get('tag')
    images_id_list = []    
    for image_id in each_cotent_stream.get("image_ids"):
        images_id_list.append(image_id.get('id'))
    
    vcsRef = get_latest_images(images_id_list)
    content_strem["vcsRef"] = vcsRef
    respose_data.append(content_strem)

#Print the final result
pprint.pprint(respose_data)