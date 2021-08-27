import cv2, math
import numpy as np
# 使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成

__author__ = "boboa"


# 标准霍夫线变换
def line_detection_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 2, np.pi/180, 200)  # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
    print(lines)
    if not lines:
        return
    for line in lines:
        rho, theta = line[0]  # line[0]存储的是点到直线的极径和极角，其中极角是弧度表示的
        a = np.cos(theta)   # theta是弧度
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))  # 直线起点横坐标
        y1 = int(y0 + 1000 * (a))   # 直线起点纵坐标
        x2 = int(x0 - 1000 * (-b))  # 直线终点横坐标
        y2 = int(y0 - 1000 * (a))   # 直线终点纵坐标
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("image_lines", image)


# 统计概率霍夫线变换
def line_detect_possible_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=5)
    # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=30)
	#math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 1)
    cv2.imshow("line_detect_possible_demo", image)


if __name__ == "__main__":
    img = cv2.imread("test-2-1.png")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    #cv2.imshow("input image", img)
    line_detect_possible_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()