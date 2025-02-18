from csv import DictReader, DictWriter

class Analysis:
    def __init__(self, emailsforcheck, comparewith):
        super().__init__()
        self.emailsforcheck = emailsforcheck
        self.comparewith = comparewith

    def read_files(self):
#       Emails for check:
        with open(self.emailsforcheck, encoding='utf-8', mode='r', newline='') as f:
            emails_for_check_list_read = DictReader(f, delimiter=',')
            emails_for_check_list = []
            for email in emails_for_check_list_read:
                emails_for_check_list_formatted = email['Email'].lower()
                emails_for_check_list.append(emails_for_check_list_formatted)
        print('Email list:\n', emails_for_check_list[0:10], '...')

#       Emails to compare with:
        with open(self.comparewith, encoding='utf-8', mode='r', newline='') as f:
            compare_with_list_read = DictReader(f, delimiter=',')
            compare_with_list = []
            for email in compare_with_list_read:
                compare_with_list_formatted = email['Email'].lower()
                compare_with_list.append(compare_with_list_formatted)
        print('Compare with list:\n', compare_with_list[0:10], '...')
        self.downloadduplicates = []
        self.downloadunique = []
        for email in emails_for_check_list:
            if email in compare_with_list:
                self.downloadduplicates.append(email)
            else:
                self.downloadunique.append(email)
        print('\n +++++++++++++Duplicates+++++++++++\n', self.downloadduplicates[0:10], '...', '\n number of duplicate entries:', len(self.downloadduplicates))
        print('\n ===============Unique=============\n', self.downloadunique[0:10], '...', '\n number of unique entries:', len(self.downloadunique))
        pass
    
    def list_duplicates(self):
        return self.downloadduplicates

    def list_unique(self):
        return self.downloadunique


    # def data_prep(self):
    # itraukti daugiau duomenu nei tik email
    # atpazinti emailus (uzrasas su "@", atskirtas " " is abeju pusiu)
    # spelioti emailus 
    # generuoti nuorodas i web-page-a.
    # pass


