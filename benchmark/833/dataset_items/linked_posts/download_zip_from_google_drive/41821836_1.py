// NOTE: FileDownloader is IDisposable!
FileDownloader fileDownloader = new FileDownloader();

// This callback is triggered for DownloadFileAsync only
fileDownloader.DownloadProgressChanged += ( sender, e ) => Console.WriteLine( "Progress changed " + e.BytesReceived + " " + e.TotalBytesToReceive );
// This callback is triggered for both DownloadFile and DownloadFileAsync
fileDownloader.DownloadFileCompleted += ( sender, e ) => Console.WriteLine( "Download completed" );

fileDownloader.DownloadFileAsync( "https://INSERT_DOWNLOAD_LINK_HERE", @"C:\downloadedFile.txt" );
