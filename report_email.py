#!/usr/bin/env python3
import os
import datetime
import reports
import emails

dt = datetime.date(datetime.now("%B,%d,%Y"))
summary = []
data = {}
path = "./supplier-data/descriptions/"
for file in os.listdir("./supplier-data/descriptions"):
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if len(line) <= 10 and len(line) > 0 and "lb"not in line:
                data["name"] = line
            if "lbs" in line:
                data["weight"] = line
        summary.append(dict(data))
summ = "<br/>".join(summary)


if __name__ == "__main__":
    reports.generate_report("./tmp/processed.pdf", dt, summ)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send_email(message)
