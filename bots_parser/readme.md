# Web Scraping General Functions #

## buttons_inputs.py ##

By now there is two functions


#### Input Value ####


Insert value in input hmtl 

| Input     | Definition                            | Required | Type |
|-----------|-----------------------	-------|-------|-------|
|  wait_obj | selenium wait obj                     |	yes    | String |
| text_input| text to be inputed at the htlm input  |   yes    | String |
| element   | selenium element                      |   yes    | String |
|input_xpath| the css of the input                |   no, if xpath   | String |
|input_xpath| the xpath of the input                |   no, if css     | String |
| enter     | send the enter key command after inputing text          | no      | Boolean |

#### Click button ####

Find a button and click 

| Input     | Definition                            | Required |
|------|------------------------------|-------|
|  wait_obj | selenium wait obj                     |	yes    |
| element   | selenium element                      |   yes    |
| button_css | the css format of the clickable           |   no,if xpath     |
|button_xpath| the xpath of the clickable                |   no, if css     |
