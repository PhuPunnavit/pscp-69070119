"""Saitama"""

def main():
    """main"""
    req_pushup = int(input())
    req_situp = int(input())
    req_squat = int(input())
    req_run = int(input())
    daily_pushup = int(input())
    daily_situp = int(input())
    daily_run = int(input())
    daily_squat = int(input())
    result_pushup = (req_pushup + daily_pushup - 1) // daily_pushup
    result_situp = (req_situp + daily_situp - 1 ) // daily_situp
    result_run = (req_run + daily_run - 1 ) // daily_run
    result_squat = (req_squat + daily_squat - 1 ) // daily_squat
    my_list = [result_pushup, result_situp, result_run, result_squat]
    print(max(my_list))

main()
