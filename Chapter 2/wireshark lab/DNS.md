# Q1
nslookup.exe us.syyx.com
服务器:  public1.alidns.com
Address:  223.5.5.5

非权威应答:
名称:    us.syyx.com.wswebcdn.com
Addresses:  120.39.212.79
          117.24.11.18
Aliases:  us.syyx.com
# Q2
nslookup.exe -type=NS cam.ac.uk
服务器:  public1.alidns.com
Address:  223.5.5.5

非权威应答:
cam.ac.uk       nameserver = auth0.dns.cam.ac.uk
cam.ac.uk       nameserver = dns0.eng.cam.ac.uk
cam.ac.uk       nameserver = ns1.mythic-beasts.com
cam.ac.uk       nameserver = ns3.mythic-beasts.com
cam.ac.uk       nameserver = dns0.cl.cam.ac.uk
cam.ac.uk       nameserver = ns2.ic.ac.uk
# Q3
nslookup.exe -type=MX yahoo.com auth0.dns.cam.ac.uk
DNS request timed out.
    timeout was 2 seconds.
服务器:  UnKnown
Address:  131.111.8.37

*** UnKnown 找不到 yahoo.com: Query refused
*seems that dns server refused the query :(*
# Q4
UDP
# Q5
destination port: 53
source port: 53
# Q6
ip in wireshark:172.17.48.1
ip from /etc/resolv.conf:172.17.48.1
# Q7
A and AAA types. no answers
# Q8
www.ietf.org: type CNAME, class IN, cname www.ietf.org.cdn.cloudflare.net
www.ietf.org.cdn.cloudflare.net: type A, class IN, addr 104.16.45.99
www.ietf.org.cdn.cloudflare.net: type A, class IN, addr 104.16.44.99
# Q9
104.16.45.99
# Q10
no
# Q11
53
# Q12
same as Q6
# Q13
A. no answers
# Q14
www.mit.edu: type CNAME, class IN, cname www.mit.edu.edgekey.net
www.mit.edu.edgekey.net: type CNAME, class IN, cname e9566.dscb.akamaiedge.net
e9566.dscb.akamaiedge.net: type A, class IN, addr 23.63.55.204
# Q15
pass
# Q16
same as Q6
# Q17
NS. no answers.
# Q18
8 answers. no ip provided.
# Q19
pass
# Q20
the first query is sent to default dns server for resolving nameserver: bitsy.mit.edu.
then the second query is sent to the bitsy.mit.edu for resolving www.aiit.or.kr
# Q21
A, no answers.
# Q22
the first answer:
- bitsy.mit.edu: type A, class IN, addr 18.0.72.3
the second one:
timeout...
# Q23
pass