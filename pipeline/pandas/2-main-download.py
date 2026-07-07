def slice_zip_from_drive(file_id, expected_csv_name):
    """Downloads the zip file locally, slices out the first 10,000 lines, and cleans up."""
    zip_filename = expected_csv_name + ".zip"
    
    print(f"\nDownloading zip archive from Google Drive...")
    gdown.download(id=file_id, output=zip_filename, quiet=False)
        
    print(f"Slicing out a lightweight copy of {expected_csv_name}...")
    
    # Using 'with' statements correctly handles closing the files
    with zipfile.ZipFile(zip_filename) as z:
        with z.open(expected_csv_name) as infile:
            lines = [infile.readline() for _ in range(10000)]
            
    # Step out of the zip file context entirely before writing the new CSV
    with open(expected_csv_name, 'wb') as outfile:
        outfile.writelines(lines)
                
    # Now that the zipfile block is completely finished and closed, Windows will let us delete it
    try:
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
            print(f"Cleaned up and removed temporary archive: {zip_filename}")
    except PermissionError:
        print(f"⚠️ Windows held a temporary lock on {zip_filename}. It's safe to ignore or delete manually later!")