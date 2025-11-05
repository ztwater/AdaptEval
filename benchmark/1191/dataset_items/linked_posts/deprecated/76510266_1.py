from library import Ham  # error: Use of deprecated class Ham. Use Spam instead.

import library

library.norwegian_blue(1)  # error: Use of deprecated function norwegian_blue. It is pining for the fiords.
map(library.norwegian_blue, [1, 2, 3])  # error: Use of deprecated function norwegian_blue. It is pining for the fiords.

library.foo(1)  # error: Use of deprecated overload for foo. Only str will be allowed.
library.foo("x")  # no error

ham = Ham()  # no error (already reported above)
