re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
filtered_string = re_pattern.sub(u'\uFFFD', unicode_string)    
