## Project Requirements Document for Django Cars

### Unit Tests

#### Check Username View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the check username URL. | When the URL for checking the username is resolved. | The resolved function should be htmx_views.check_username. | test_check_username_url_is_resolved
The check username view must handle POST requests correctly when the username already exists. | When a POST request is made to the check username URL with an existing username. | The response should have a status code of 200. The response content should be This username already exists. | test_check_username_post_existing_username
The check username view must handle POST requests correctly when the username is new. | When a POST request is made to the check username URL with a new username. | The response should have a status code of 200. The response content should be This username is available. | test_check_username_post_new_username

#### Add Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the add car URL. | When the URL for adding a car is resolved. | The resolved function should be htmx_views.add_car. | test_add_car_url_is_resolved
The add car view must handle POST requests by anonymous users correctly. | When a POST request is made to the add car URL by an anonymous user. | The response should have a status code of 302. | test_add_car_post_anonymous_user
The add car view must handle POST requests by authenticated users correctly. | When a POST request is made to the add car URL by an authenticated user. | The response should have a status code of 200. | The context dictionary should include cars with the newly added car producer audi. The response should use the partials/car_list.html template. | test_add_car_post_authenticated_user

#### Delete Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the delete car URL. | When the URL for deleting a car is resolved. | The resolved function should be htmx_views.delete_car. | test_delete_car_url_is_resolved
The delete car view must handle GET requests by anonymous users correctly. | When a GET request is made to the delete car URL by an anonymous user. | The response should have a status code of 302. | test_delete_car_get_anonymous_user
The delete car view must handle DELETE requests by authenticated users correctly. | When a DELETE request is made to the delete car URL by an authenticated user. The response should have a status code of 200. | The context dictionary should include cars with no cars left. The response should use the partials/car_list.html template. | test_delete_car_get_authenticated_user

#### Search Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the search car URL. | When the URL for searching a car is resolved. | The resolved function should be htmx_views.search_car. | test_search_car_url_is_resolved
The search car view must handle POST requests by anonymous users correctly. | When a POST request is made to the search car URL by an anonymous user. | The response should have a status code of 302. | test_search_car_post_anonymous_user
The search car view must handle POST requests by authenticated users correctly. | When a POST request is made to the search car URL by an authenticated user. | The response should have a status code of 200. The context dictionary should include results with the car producer porshe. The response should use the partials/search_results.html template. | test_search_car_post_authenticated_user

#### Detail Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the detail URL. | When the URL for car detail is resolved. | The resolved function should be htmx_views.detail. | test_detail_url_is_resolved
The detail view must handle GET requests by anonymous users correctly. | When a GET request is made to the detail URL by an anonymous user. | The response should have a status code of 302. | test_detail_get_anonymous_user
The detail view must handle GET requests by authenticated users correctly. | When a GET request is made to the detail URL by an authenticated user. | The response should have a status code of 200. The context dictionary should include user_car with the car producer audi. The response should use the partials/car_detail.html template. | test_detail_get_authenticated_user

#### Cars Partial View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the car list partial URL. | When the URL for the car list partial is resolved. | The resolved function should be htmx_views.cars_partial. | test_cars_partial_url_is_resolved
The car list partial view must handle GET requests by anonymous users correctly. | When a GET request is made to the car list partial URL by an anonymous user. | The response should have a status code of 302. | test_cars_partial_get_anonymous_user
The car list partial view must handle GET requests by authenticated users correctly. | When a GET request is made to the car list partial URL by an authenticated user. | The response should have a status code of 200. The context dictionary should include cars. The response should use the partials/car_list.html template. | test_cars_partial_get_authenticated_user

#### Upload Photo View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the upload photo URL. | When the URL for uploading a photo is resolved. | The resolved function should be htmx_views.upload_photo. | test_upload_photo_url_is_resolved
The upload photo view must handle POST requests by anonymous users correctly. | When a POST request is made to the upload photo URL by an anonymous user. | The response should have a status code of 302. | test_upload_photo_post_anonymous_user
The upload photo view must handle POST requests by authenticated users correctly. | When a POST request is made to the upload photo URL by an authenticated user. | The response should have a status code of 200. The context dictionary should include user_car. The response should use the partials/car_detail.html template. | test_upload_photo_post_authenticated_user

#### Clear View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the clear URL. | When the URL for clearing data is resolved. | The resolved function should be htmx_views.clear. | test_clear_url_is_resolved
The clear view must handle GET requests correctly. | When a GET request is made to the clear URL. | The response should have a status code of 200. The response content should be empty. | test_clear_get

#### Sort View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the sort URL. | When the URL for sorting data is resolved. | The resolved function should be htmx_views.sort. | test_sort_url_is_resolved
The sort view must handle GET requests correctly. | When a GET request is made to the sort URL. | The response should have a status code of 200. The response should use the partials/car_list.html template. | test_sort_get

#### Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200, use the index.html template. The response must contain the text 'My Rides Home Page'. | test_index_get
The index URL must resolve to the correct view. | When the index URL is resolved. | The URL should resolve to HomeView. | test_index_url_is_resolved

#### Register View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The register view must handle GET requests correctly. | When a GET request is made to the register URL. | The response should have a status code of 200, use the register.html template. The response must contain the text 'My Rides Register'. | test_register_get
The register view must handle POST requests correctly. | When a POST request is made to the register URL with valid user data. | The response should have a status code of 200, use the login.html template. The response must contain the text 'My Rides Login'. | test_register_post
The register URL must resolve to the correct view. | When the register URL is resolved. | The URL should resolve to RegisterView. | test_register_url_is_resolved

#### Login View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The login view must handle GET requests correctly. | When a GET request is made to the login URL. | The response should have a status code of 200, use the login.html template. The response must contain the text 'My Rides Login'. | test_login_get
The login view must handle POST requests correctly. | When a POST request is made to the login URL with valid user credentials. | The response should have a status code of 200, use the login.html template. The response must contain the text 'My Rides Login'. | test_login_post
The login URL must resolve to the correct view. | When the login URL is resolved. | The URL should resolve to Login. | test_login_url_is_resolved

#### Logout View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The logout URL must resolve to the correct view. | When the logout URL is resolved. | The URL should resolve to LogoutView. | test_logout_url_is_resolved

#### Car List View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The car list view must handle GET requests correctly for authenticated users. | When an authenticated user makes a GET request to the car list URL. | The response should have a status code of 200, use the cars.html template. The response must contain the text 'My Rides Cars List'. | test_car_list_get_authenticated_user
The car list view must handle GET requests correctly for anonymous users. | When an anonymous user makes a GET request to the car list URL. | The response should have a status code of 302 (redirect). | test_car_list_get_anonymous_user
The car list view must provide the correct context for authenticated users. | When an authenticated user makes a GET request to the car list URL. | The response context should include the user's cars. | The context should contain the car with the producer 'porshe'. | test_car_list_context
The car list URL must resolve to the correct view. | When the car list URL is resolved. | The URL should resolve to CarList. | test_car_list_url_is_resolved


#### Utility Functions Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The get_max_order function must return the next order number correctly for a user with existing cars. | When the get_max_order function is called with a user object that has existing cars. | The function should return expected value. | test_get_max_order_existing_cars
The get_max_order function must return the initial order number correctly for a user with no existing cars. | When the get_max_order function is called with a user object that has no existing cars. | The function should expected value. | test_get_max_order_no_cars
The reorder function must correctly reorder the cars for a user with existing cars after a deletion. | When the reorder function is called with a user object after deleting a car. | The remaining cars should be reordered correctly, with the audi car having an order of 1. | test_reorder_existing_cars
The reorder function must handle cases where the user has no cars correctly. | When the reorder function is called with a user object that has no existing cars. | The function should return None. | test_reorder_no_cars

### Selenium Tests

#### Home Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The home page must display the correct title. | When the home page is loaded. | The page title should be 'My Rides Home Page'. | is_title_matches
The home page must display the correct heading. | When the home page is loaded. | The heading should contain the text 'RIDES BY MJ'. | is_home_heading_displayed_correctly
The register link on the home page must navigate to the register page correctly. | When the register link is clicked. | The page title should be 'My Rides Register'. | is_register_link_works
The login link on the home page must navigate to the login page correctly. | When the login link is clicked. | The page title should be 'My Rides Login'. | is_login_link_works
The home link must navigate back to the home page correctly. | When the home link is clicked. | The page title should be 'My Rides Home Page'. | is_home_link_works

#### Register Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The register page must display the correct title. | When the register page is loaded. | The page title should be 'My Rides Register'. | is_title_matches
The registration form must submit correctly with valid data. | When valid data is entered and the form is submitted. | The user should be redirected to the login page and the page title should be 'My Rides Login'. | is_register_form_works

#### Login Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The login page must display the correct title. | When the login page is loaded. | The page title should be 'My Rides Login'. | is_title_matches
The login form must submit correctly with valid credentials. | When valid credentials are entered and the form is submitted. | The user should see a 'LOGOUT' link indicating successful login. | is_login_form_works
The logout link must log the user out and redirect to the home page. | When the logout link is clicked. | The user should be redirected to the home page and the page title should be 'My Rides Home Page'. | is_logout_link_works

#### Cars List Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The cars list page must display the correct title. | When the cars list page is loaded. | The page title should be 'My Rides Cars List'. | is_title_matches
The cars list link must navigate to the cars list page correctly. | When the cars list link is clicked. | The page title should be 'My Rides Cars List'. | is_cars_list_link_works
The cars list page must display the correct heading. | When the cars list page is loaded. | The heading should contain the text 'MY CARS'. | is_cars_list_heading_displayed_correctly
The cars list page must display the correct message when no cars are present. | When the user has no cars. | The page should display the text 'YOU DO NOT HAVE CARS YET...'. | is_no_cars_para_displayed_correctly
The search cars form must work correctly with valid data. | When valid data is entered and the form is submitted. | The list should update and display the searched car, e.g., 'PORSHE'. | is_search_cars_form_works
The add car form must submit correctly with valid data. | When valid data is entered and the form is submitted. | A message should display confirming the addition of the car, e.g., 'ADDED AUDI TO LIST OF CARS'. | is_add_car_form_works







