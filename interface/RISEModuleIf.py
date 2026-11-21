"""IoT 모듈의 기본 인터페이스.

``functions/<모듈명>/Impl.py`` 는 이 클래스를 상속한 ``RISEModule`` 을 정의한다.
수명 주기 메서드 외의 공개 메서드는 gRPC 로 이름을 지정해 호출할 수 있다.
"""


class RISEModuleIf:
    def enterAction(self) -> None:
        """모듈이 로드된 직후 1회 호출된다. (연결 수립 등)"""

    def leaveAction(self) -> None:
        """모듈이 리로드되기 직전, 또는 서버 종료 시 호출된다. (자원 해제 등)"""
