// IPv6 textual representation validating parser fully compliant with RFC-4291 and RFC-5952
// BSD-licensed / Copyright 2015-2017 Alexandre Fenyo

#include <string.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

typedef enum { false, true } bool;

static const char hexdigits[] = "0123456789abcdef";
static int digit2int(const char digit) {
  return strchr(hexdigits, digit) - hexdigits;
}

// This IPv6 address parser handles any valid textual representation according to RFC-4291 and RFC-5952.
// Other representations will return -1.
//
// note that str input parameter has been modified when the function call returns
//
// parse_ipv6(char *str, struct in6_addr *retaddr)
// parse textual representation of IPv6 addresses
// str:     input arg
// retaddr: output arg
int parse_ipv6(char *str, struct in6_addr *retaddr) {
  bool compressed_field_found = false;
  unsigned char *_retaddr = (unsigned char *) retaddr;
  char *_str = str;
  char *delim;

  bzero((void *) retaddr, sizeof(struct in6_addr));
  if (!strlen(str) || strchr(str, ':') == NULL || (str[0] == ':' && str[1] != ':') ||
      (strlen(str) >= 2 && str[strlen(str) - 1] == ':' && str[strlen(str) - 2] != ':')) return -1;

  // convert transitional to standard textual representation
  if (strchr(str, '.')) {
    int ipv4bytes[4];
    char *curp = strrchr(str, ':');
    if (curp == NULL) return -1;
    char *_curp = ++curp;
    int i;
    for (i = 0; i < 4; i++) {
      char *nextsep = strchr(_curp, '.');
      if (_curp[0] == '0' || (i < 3 && nextsep == NULL) || (i == 3 && nextsep != NULL)) return -1;
      if (nextsep != NULL) *nextsep = 0;
      int j;
      for (j = 0; j < strlen(_curp); j++) if (_curp[j] < '0' || _curp[j] > '9') return -1;
      if (strlen(_curp) > 3) return -1;
      const long val = strtol(_curp, NULL, 10);
      if (val < 0 || val > 255) return -1;
      ipv4bytes[i] = val;
      _curp = nextsep + 1;
    }
    sprintf(curp, "%x%02x:%x%02x", ipv4bytes[0], ipv4bytes[1], ipv4bytes[2], ipv4bytes[3]);
  }

  // parse standard textual representation
  do {
    if ((delim = strchr(_str, ':')) == _str || (delim == NULL && !strlen(_str))) {
      if (delim == str) _str++;
      else if (delim == NULL) return 0;
      else {
        if (compressed_field_found == true) return -1;
        if (delim == str + strlen(str) - 1 && _retaddr != (unsigned char *) (retaddr + 1)) return 0;
        compressed_field_found = true;
        _str++;
        int cnt = 0;
        char *__str;
        for (__str = _str; *__str; ) if (*(__str++) == ':') cnt++;
        unsigned char *__retaddr = - 2 * ++cnt + (unsigned char *) (retaddr + 1);
        if (__retaddr <= _retaddr) return -1;
        _retaddr = __retaddr;
      }
    } else {
      char hexnum[4] = "0000";
      if (delim == NULL) delim = str + strlen(str);
      if (delim - _str > 4) return -1;
      int i;
      for (i = 0; i < delim - _str; i++)
        if (!isxdigit(_str[i])) return -1;
        else hexnum[4 - (delim - _str) + i] = tolower(_str[i]);
      _str = delim + 1;
      *(_retaddr++) = (digit2int(hexnum[0]) << 4) + digit2int(hexnum[1]);
      *(_retaddr++) = (digit2int(hexnum[2]) << 4) + digit2int(hexnum[3]);
    }
  } while (_str < str + strlen(str));
  return 0;
}
