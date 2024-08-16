from OpenGL.GL import *
# from OpenGL.GLUT import *
from PySide2.QtWidgets import QOpenGLWidget


class Page1(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def initializeGL(self):
        glClearColor(0.2, 0.4, 0.52, 1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        side = min(w, h)
        if side < 0:
            return

        # 视口
        glViewport((w - side) // 2, (h - side) // 2, side, side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # 正交投射
        glOrtho(-1.5, 1.5, -1.5, 1.5, -10, 10)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glBegin(GL_TRIANGLES)
        glColor3d(1.0, 0.0, 0.0)
        glVertex3d(0.0, 1.0, 0.0)
        glColor3d(0.0, 1.0, 0.0)
        glVertex3d(-1.0, -1.0, 0.0)
        glColor3d(0.0, 0.0, 1.0)
        glVertex3d(1.0, -1.0, 0.0)
        glEnd()
