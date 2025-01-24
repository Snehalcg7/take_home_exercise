#To run the code on Linux terminal

- Pre-requisites : Python

- Steps :
    1] Open a terminal
    2] Navigate to the script's directory
    3] Run the python script - python main.py


#Implementation of code

- Requirement :
   To get a report showing information on the most recent image in each content stream for rhbk/keycloakrhel9.
   The report should be in JSON format with the following keys, per content stream.

   The keys’ values shown here are examples:
   {
     "contentStream": "26.0",
     "vcsRef": "84d4042f71c665c0636aa5ffda537f52c21aa06c",
     "publishedDate": "2024-11-13T14:10:23+00:00",
     "freshnessGrade": "A"
   }

- Description :

  1] Got the content streams data fields by using Red Hat Ecosystem Catalog’s public API by providing registry name and repository name
  2] Stored all the images' Ids corresponding to the each Content stream
  3] Passed the list of images Ids to a function 'get_latest_images'
  4] Got the additional required fields of images by using API call and filtering response by required fields only
  5] Sorted the images by last modified date and returned the field values of latest image
  6] stored the response in the list as per the content streams
  7] Printed out the final result in respose_data

