import dns.resolver
import sys

def lookup_mx(domain_name):
    try:
        answers = dns.resolver.query(domain_name, 'MX')
        mx_records = ['alt1.aspmx.l.google.com.',
                      'alt2.aspmx.l.google.com.',
                      'alt3.aspmx.l.google.com.',
                      'alt4.aspmx.l.google.com.',
                    'aspmx.l.google.com.' ]
        for rdata in answers:
            if str(rdata.exchange).lower() in mx_records:
                return True
            else:
                return False
    except:
        return False
		
try:
	#READ MASSIVE FILE
	with open("doms.txt") as f:
		for line in f:
			domain_name = line.replace("\n","")
			g = lookup_mx(domain_name)
			if g:
				text_file = open("gsuite.txt", "a")
				text_file.write(""+domain_name+"\n")
				text_file.close()
				print ("[*] "+domain_name+" has MX Records for G-suite [*] ")
			else:
				print ("[*] "+domain_name+" is not pointing at G-suite [*] ")
		
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
