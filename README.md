# Getting Started

## Setup

1. Get the code repository
  - `git clone https://github.com/abhijeetdtu/bootcamps`

2. Setup the bootcamp registration sheet link
  1. Go to Google Form for registration for this semester
  2. Go to the linked Google Sheet for this form
  3. Copy the ID of the sheet and place it in `./bootcamps/bootcamps/config.py`
    - ![image](https://user-images.githubusercontent.com/6872080/111344658-f0c7d380-8652-11eb-8fda-6d61354e0f91.png)
    - ![image](https://user-images.githubusercontent.com/6872080/111344865-253b8f80-8653-11eb-9614-f974ce0f6b28.png)

3. Enable Google API access
 - Follow [Google Guide](https://developers.google.com/sheets/api/quickstart/python) to authorize your `@uncc.edu` email id to access Google Sheets API
 - Download the `credentials.json` and place it in `./bootcamps/bootcamps`

4. Download DB Browser SQL LITE
   - https://sqlitebrowser.org/

5. Initialize the local database
  - Go to root of the cloned repository
  - run `python -m pip install -r requirements.txt`
  - run `python -m bootcamps.bl.dbsetup`
  - NOTE : There is an already existing bootcamp.db file. This is from the previous semester and you may want to keep it for archival/analytical purposes
  - You can validate that things really worked by loading bootcamp.db from `./bootcamps` into DB browser
    - ![image](https://user-images.githubusercontent.com/6872080/111346242-6aac8c80-8654-11eb-8a30-11f76721e04e.png)
    - You will see a bunch of tables/views - which will be empty as of now
      - ![image](https://user-images.githubusercontent.com/6872080/111346309-79933f00-8654-11eb-9c35-2555e62914f1.png)


All good to go now!

## Common Tasks
NOTE : All commands below to be executed from root of the cloned repository i.e `./bootcamps/`

1. Checking registrations
  - `python -m bootcamps.bl.sheet_db_loader --load-register`
  - Now in DB Browser you will see the *view* **registration_process** populated with users that need to be added manually in **Canvas**
    - ![image](https://user-images.githubusercontent.com/6872080/111346484-a2b3cf80-8654-11eb-97c9-4b45cc19a545.png)

2. Updating grades and Sending Certificates
  1. Updating Grades
    - For each bootcamp download the grade book and place it in `./bootcamps/bootcamps/dumps`
      - NOTE: delete any previous grade book in the folder
    - Run - `python -m bootcamps.bl.sheet_db_loader --load-grades`
    - Now in DB Browser you will see the *view* **grades_tracker** populated
      - ![image](https://user-images.githubusercontent.com/6872080/111346853-00e0b280-8655-11eb-85b0-dabf751189fd.png)
  2. Sending Certificates
    - Now with Grades updated you can automatically generate certificates for eligible students
      - Eligibility is determined by `./bootcamps/bootcamps/sql/fetch_cert_send.sql`
        - This generally uses 90% as the threshold for the bootcamps
        - For stats course there is additional check for `comprehensive test` completion
    - Run : `python -m bootcamps.bl.cert_send`
      - This will populate certificates in `./bootcamps/bootcamps/certgen/outputs`
      - The `pdf` versions are sent out to the students manually
      - Name of each file is formatted as - `<LOGIN_ID>_<RANDOM_HEX>`
        - Use LOGIN_ID@uncc.edu as the email address for that certificate
        - I personally have used a Gmail Template to quickly attach and send the certs
          - ![image](https://user-images.githubusercontent.com/6872080/111347531-b0b62000-8655-11eb-88d2-5804f731d501.png)


### Appendix:

I have locally cloned the repository in `C:\Users\Abhijeet\Documents\Github`
therefore usual chain of commands is

`cd .\Documents\Github\bootcamps
python -m bootcamps.bl.sheet_db_loader --load-grades
python -m bootcamps.bl.cert_send
`
