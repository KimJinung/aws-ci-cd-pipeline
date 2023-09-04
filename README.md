# aws-ci-cd-pipeline
AWS CI/CD 솔루션을 활용하여 컨테이너 기반 API를 자동으로 빌드하고 배포합니다.

![AWS_CI_CD_Pipeline-3](https://github.com/KimJinung/aws-ci-cd-pipeline/assets/111354195/9ac28203-d624-4339-8bff-4e8929babb65)

---
## CI/CD 파이프라인 흐름
1. CodePipeline에서 main 브랜치의 변경 사항을 감지하고, CodeBuild 프로젝트를 트리거합니다.
2. CodeBuild는 소스 코드 테스트, 컨테이너 이미지 빌드 후 ECR에 신규 이미지를 푸쉬합니다.
3. 람다가 사용하는 컨테이너 이미지 버전을 latest로 업데이트 합니다.

- AWS CodeBuild에서 CD까지 처리합니다.
- stage를 추가하고 CodeDeploy에 CD를 분리하는 방법으로 Code review 및 approval 과정을 추가할 수 있습니다.
----

