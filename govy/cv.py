import deeplabcut
import glob
import os

'''
참고 가이드
https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html
'''


# 파일 이름
project_title = "망둑어 데이터셋 저장"
experimenter = "Kingdaehan" 
key_points = ['nose', 'forehead', 'mouth-corner', 'mouth-center', 'neck']
skeleton = [['nose', 'forehead'], ['nose', 'mouth-center'],
      ['mouth-center', 'mouth-corner'], ['forehead', 'neck']]


# 비디오 경로
video_path = ['./videos/example1.mp4', './videos/example2.mp4'] #예시 비디오

# 프로젝트 생성
deeplabcut.create_new_project(project_title, experimenter, video_path,
         copy_videos=True, multianimal=False)

# multianimal : 영상에 동물 여러마리 인지?

# config.yaml 파일 경로 설정(절대경로) 및 수정
config_path = os.getcwd() + ‘/config.yaml’
edits = {
        'bodyparts': key_points,
        'skeleton': skeleton
}

deeplabcut.auxiliaryfunctions.edit_config(config_path, edits)

# 영상 추가
deeplabcut.add_new_videos(config_path, ['Full path of video 1', ...], copy_videos=True)


# 프레임 추출 (설정 잘 참고하세요)
deeplabcut.extract_frames(config_path, mode='automatic/manual', algo='uniform/kmeans', userfeedback=False, crop=True/False)

# 프레임 라벨링
deeplabcut.label_frames(config_path)

'''
# 라벨링 확인[Optional ]
#deeplabcut.check_labels(config_path, visualizeindividuals=True/False)
'''

# 영상 분석
video_list = glob.glob(os.getcwd() + '/videos/*.mp4') # 테스트할 영상 경로 입력하기
deeplabcut.analyze_videos(config_path, video_list, dynamic=(True, .5, 10))

# 영상 생성
deeplabcut.create_labeled_video(config_path, video_list, filtered=True)