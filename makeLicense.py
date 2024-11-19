import json
import os
import sys

def read_py_license_file(filename):
    """Read Python license file format and extract license texts"""
    try:
        with open(filename) as f:
            data = json.load(f)
        
        license_texts = []
        for item in data:
            if 'LicenseText' in item:
                header = f"\n\n{'='*80}\n{item['Name']} {item['Version']}\n{'='*80}\n"
                license_texts.append(header + item['LicenseText'])
        
        return license_texts
    except Exception as e:
        print(f"Error reading Python license file {filename}: {str(e)}", file=sys.stderr)
        return []

def read_js_license_file(filename):
    """Read JavaScript/TypeScript license file format and extract license texts"""
    try:
        with open(filename) as f:
            data = json.load(f)
        
        license_texts = []
        for package, info in data.items():
            if 'licenseFile' in info:
                try:
                    with open(info['licenseFile']) as f:
                        license_text = f.read()
                    header = f"\n\n{'='*80}\n{package}\n{'='*80}\n"
                    license_texts.append(header + license_text)
                except Exception as e:
                    print(f"Error reading license file for {package}: {str(e)}", file=sys.stderr)
                    
            if 'noticeFile' in info:
                try:
                    with open(info['noticeFile']) as f:
                        notice_text = f.read()
                    header = f"\n\nNOTICE for {package}:\n"
                    license_texts.append(header + notice_text)
                except Exception as e:
                    print(f"Error reading notice file for {package}: {str(e)}", file=sys.stderr)
                    
        return license_texts
    except Exception as e:
        print(f"Error reading JavaScript/TypeScript license file {filename}: {str(e)}", file=sys.stderr)
        return []

def main():
    # Read all license files
    py_licenses = read_py_license_file('third-party-licenses-py-job-runner.json')
    ts_licenses = read_js_license_file('third-party-licenses-ts-job-runner.json')
    gh_licenses = read_js_license_file('third-party-licenses-benchify-github.json')
    
    # Combine all license texts
    all_licenses = py_licenses + ts_licenses + gh_licenses
    
    # Write combined output
    try:
        with open('LICENSE.txt', 'w') as f:
            f.write("THIRD PARTY LICENSES\n\n")
            f.write("This file contains the licenses for all third party dependencies.\n")
            for license_text in all_licenses:
                f.write(license_text)
    except Exception as e:
        print(f"Error writing LICENSE.txt: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

