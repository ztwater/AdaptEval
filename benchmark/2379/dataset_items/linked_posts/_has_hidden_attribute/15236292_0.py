import Foundation

def is_hidden(path):
    url = Foundation.NSURL.fileURLWithPath_(path)
    return url.getResourceValue_forKey_error_(None, Foundation.NSURLIsHiddenKey, None)[0]

def listdir_skipping_hidden(path):
    url = Foundation.NSURL.fileURLWithPath_(path)
    fm = Foundation.NSFileManager.defaultManager()
    urls = fm.contentsOfDirectoryAtURL_includingPropertiesForKeys_options_error_(
        url, [], Foundation.NSDirectoryEnumerationSkipsHiddenFiles, None)[0]
    return [u.path() for u in urls]
