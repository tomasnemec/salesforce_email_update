# Salesforec email update with Dataloader

# Prerequisites
*  Mailbox export in `.csv` format
*  Data Loader application

# Suggestions
*  If you can not extport a mailbox content straigth into .csv format, there is an option (in Gmail mailbox) to have teh mailbox downloaded as .mbox. 
*  Then you can use [MBOX to CSV Converter](https://apps.apple.com/us/app/mbox-to-csv-converter/id1099737378?ls=1&mt=12) to get the right format.

*  [Data Loader](https://help.salesforce.com/articleView?id=data_loader.htm&type=5) can be download directly from your Salesforce instance.

# How it works!**
1. Export mailbox content, convert it to .csv format and place the file named as `file.csv` into main directory.

2. Beforce import is done, it's necessary to create csv file `contact_id.csv` - example file. This file consists of contact email and it's salesforce id. You can generate this file using Data Loader where you connect to your production instance and export Email and Id of contact (select email, id from contact).

3. Now when you have `contact_id.csv` file updated with your data, run `salesforce_csv_update.py` file in your terminal.

4. Once the file is converted, use Data Loader > Import to import `newfile0` and `newfile1` if not empty into "Email Message" object. Select right mapping.

<img src="https://gitlab.skypicker.com/tomas.nemec/salesforce_email_update/-/raw/master/cs1.png"  alt="sc1" width="50%" height="50%"/>

<img src="https://gitlab.skypicker.com/tomas.nemec/salesforce_email_update/-/raw/master/sc2.png"  alt="sc2" width="20%" height="20%"/>


5. You should see than all emails mappen in "Email Message object"


# Extra
*  If you have multiple .csv files you need to import, you can move them all into `csvtomerge` folder and run `mergecsv.py` in your terminal. This will merge all .csv file in that folder.
