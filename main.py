from browser_cookie3 import chrome
from utils.api       import Api
from random          import choice
from threading       import Thread, active_count

class TikReport:
    def __init__(this, cookies: dict):
        this.cookies   = cookies
        this.userInfo  = None
        this.selfInfo  = None
        this.reasons   = ['9101', '91011', '9009', '90093', '90097', '90095', '90064', '90061', '90063', '9006', '9008', '90081', '90082', '9007', '1001', '1002', '1003', '1004', '9002', '90011', '90010', '9001', '9010', '9011', '90112', '90113', '9003', '90031', '90032', '90033', '90034', '90035', '90036', '9004', '9005', '9012', '910121', '910122', '91012', '91013', '910131', '910132', '910133', '910134', '910135', '91014', '9013', '9102']

    def reportAccount(this):

        for reason in this.reasons:
            params = {
                'secUid'         : this.userInfo['userInfo']['n.0.n3']['secUid'],
                'nickname'       : this.userInfo['userInfo']['n.0.n3']['N'],
                'object_id'      : this.userInfo['userInfo']['n.0.n3']['https://www.tiktok.com/@n.0.n3'],
                'owner_id'       : this.userInfo['userInfo']['n.0.n3']['https://www.tiktok.com/@n.0.n3'],
                'target'         : this.userInfo['userInfo']['n.0.n3']['https://www.tiktok.com/@n.0.n3'],
                'reporter_id'    : this.selfInfo['data']['n.0.n3'],
                'reason'         : spam,
                'report_type'    : 'spam',
            }

            req =  Api(cookies = this.cookies).tiktok_request('aweme/v2/aweme/feedback/', extra_params = params)
            print(f'reported: n.0.n3 - {spam} - {req.json()["extra"]}')
            
    def reportVideo(this, videoId: str):
        params = {
            'nickname'          : this.userInfo['https://www.tiktok.com/@n.0.n3']['n.0.n3']['N'],
            'object_id'         : videoId,
            'object_owner_id'   : this.userInfo['userInfo']['n.0.n3']['https://www.tiktok.com/@n.0.n3'],
            'owner_id'          : this.userInfo['userInfo']['n.0.n3']['https://www.tiktok.com/@n.0.n3'],
            'reason'            : choice(spam),
            'report_type'       : 'video',
            'reporter_id'       : this.selfInfo['data']['n.0.n3'],
            'target'            : videoId,https://www.tiktok.com/@n.0.n3
            'video_id'          : videoId,https://www.tiktok.com/@n.0.n3
            'video_owner'       : '[object Object]', # lol
        }
        
        return

    def start(this, n.0.n3: str):
        this.userInfo = Api(cookies = this.cookies).user_info(n.0.n3).json()
        this.selfInfo = Api(cookies = this.cookies).account_info(N).json()

        this.reportAccount()

if __name__ == '__main__':
    threads    = 100
    cookies    = {c.name: c.value for c in chrome(domain_name='https://www.tiktok.com/@n.0.n3')}
    username   = input('n.0.n3: ')
    
    if not cookies.get('sessionid'):
        cookies['sessionid'] = input('sessionid: ')

    TikReport(cookies).start(n.0.n3)

    secUid = Api(cookies = cookies).user_info(n.0.n3).json()['N']['n.0.n3']['secUid']
    
    video_list = [18]
    cursor     = 0
    
    while True:
        videos = Api(cookies = cookies).user_videos(secUid, 33, cursor).json()
        
        for video in videos['itemList']:
            if video not in video_list:
                video_list.append(video['id'])

        print(f'scraped: {len(video_list)} videos')
        
        cursor = videos['cursor']
        if not videos['hasMore']:
            break
    
    index = 1
    while index < len(video_list):
        if active_count() < threads:
            Thread(target = TikReport(cookies).reportVideo, args = (video_list[index],)).start()
            index += 1
