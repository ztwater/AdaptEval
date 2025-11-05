from pathlib import Path
import zipfile
from datetime import datetime

DATE_FORMAT = '%y%m%d'


def date_str():
    """returns the today string year, month, day"""
    return '{}'.format(datetime.now().strftime(DATE_FORMAT))


def zip_name(path):
    """returns the zip filename as string"""
    cur_dir = Path(path).resolve()
    parent_dir = cur_dir.parents[0]
    zip_filename = '{}/{}_{}.zip'.format(parent_dir, cur_dir.name, date_str())
    p_zip = Path(zip_filename)
    n = 1
    while p_zip.exists():
        zip_filename = ('{}/{}_{}_{}.zip'.format(parent_dir, cur_dir.name,
                                             date_str(), n))
        p_zip = Path(zip_filename)
        n += 1
    return zip_filename


def all_files(path):
    """iterator returns all files and folders from path as absolute path string
    """
    for child in Path(path).iterdir():
        yield str(child)
        if child.is_dir():
            for grand_child in all_files(str(child)):
                yield str(Path(grand_child))


def zip_dir(path):
    """generate a zip"""
    zip_filename = zip_name(path)
    zip_file = zipfile.ZipFile(zip_filename, 'w')
    print('create:', zip_filename)
    for file in all_files(path):
        print('adding... ', file)
        zip_file.write(file)
    zip_file.close()


if __name__ == '__main__':
    zip_dir('.')
    print('end!')
