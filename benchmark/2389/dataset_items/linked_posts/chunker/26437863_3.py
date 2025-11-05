    messages = a_generator_which_would_not_be_smart_as_a_list
    for idx, batch in groupby(messages, lambda x: x/1000):
        batch_request = BatchHttpRequest()
        for message in batch:
            batch_request.add(self.service.users().messages().modify(userId='me', id=message['id'], body=msg_labels))
        http = httplib2.Http()
        self.credentials.authorize(http)
        batch_request.execute(http=http)
