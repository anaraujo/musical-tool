page_token = None
while True:
    response = drive_service.files().list(q="mimeType='image/jpeg'",
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
        # Process change
        print 'Found file: %s (%s)' % (file.get('name'), file.get('id'))
    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

