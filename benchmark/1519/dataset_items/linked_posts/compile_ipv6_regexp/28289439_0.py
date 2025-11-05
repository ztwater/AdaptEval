class IPv6
{
    public List<string> FindIPv6InFile(string filePath)
    {
        Char ch;
        StringBuilder sbIPv6 = new StringBuilder();
        List<string> listIPv6 = new List<string>();
        StreamReader reader = new StreamReader(filePath);
        do
        {
            bool hasColon = false;
            int length = 0;

            do
            {
                ch = (char)reader.Read();

                if (IsEscapeChar(ch))
                    break;

                //Check the first 5 chars, if it has colon, then continue appending to stringbuilder
                if (!hasColon && length < 5)
                {
                    if (ch == ':')
                    {
                        hasColon = true;
                    }
                    sbIPv6.Append(ch.ToString());
                }
                else if (hasColon) //if no colon in first 5 chars, then dont append to stringbuilder
                {
                    sbIPv6.Append(ch.ToString());
                }

                length++;

            } while (!reader.EndOfStream);

            if (hasColon && !listIPv6.Contains(sbIPv6.ToString()) && IsIPv6(sbIPv6.ToString()))
            {
                listIPv6.Add(sbIPv6.ToString());
            }

            sbIPv6.Clear();

        } while (!reader.EndOfStream);
        reader.Close();
        reader.Dispose();

        return listIPv6;
    }

    public List<string> FindIPv6InText(string text)
    {
        StringBuilder sbIPv6 = new StringBuilder();
        List<string> listIPv6 = new List<string>();

        for (int i = 0; i < text.Length; i++)
        {
            bool hasColon = false;
            int length = 0;

            do
            {
                if (IsEscapeChar(text[length + i]))
                    break;

                //Check the first 5 chars, if it has colon, then continue appending to stringbuilder
                if (!hasColon && length < 5)
                {
                    if (text[length + i] == ':')
                    {
                        hasColon = true;
                    }
                    sbIPv6.Append(text[length + i].ToString());
                }
                else if (hasColon) //if no colon in first 5 chars, then dont append to stringbuilder
                {
                    sbIPv6.Append(text[length + i].ToString());
                }

                length++;

            } while (i + length != text.Length);

            if (hasColon && !listIPv6.Contains(sbIPv6.ToString()) && IsIPv6(sbIPv6.ToString()))
            {
                listIPv6.Add(sbIPv6.ToString());
            }

            i += length;
            sbIPv6.Clear();
        }

        return listIPv6;
    }

    bool IsEscapeChar(char ch)
    {
        if (ch != ' ' && ch != '\r' && ch != '\n' && ch!='\t')
        {
            return false;
        }

        return true;
    }

    bool IsIPv6(string maybeIPv6)
    {
        IPAddress ip;
        if (IPAddress.TryParse(maybeIPv6, out ip))
        {
            return ip.AddressFamily == AddressFamily.InterNetworkV6;
        }
        else
        {
            return false;
        }
    }

}
