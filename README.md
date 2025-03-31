# 📐 Cubic Spline Interpolation Analysis

This project investigates two widely-used interpolation techniques—**Natural Cubic Spline** and **Clamped Cubic Spline**—to approximate polynomial functions. It includes both a theoretical write-up and a fully functional Python implementation that visualizes and compares the methods.

This project is featured on my [personal website](https://yourwebsite.com) as part of my academic portfolio.

## 🧮 Techniques Used
- **Natural Cubic Spline Interpolation**
- **Clamped Cubic Spline Interpolation**
- Error analysis based on established interpolation bounds
- Visualization of interpolation accuracy

## 📁 Files
- `cubicSplineProject.pdf`: Full project report detailing mathematical background, derivation, and results
- `CubicSplineInterpolation.py`: Python implementation comparing natural and clamped cubic splines

## 📊 Results Summary
- The **Clamped Cubic Spline** provided a more accurate approximation of the test function compared to the natural spline.
- Both methods' errors were verified to fall within theoretical error bounds.
- Additional experiments demonstrated that increasing the number of interpolation nodes improves approximation accuracy.

## 📦 Dependencies
- `numpy`
- `scipy`
- `matplotlib`

You can install them using:

```bash
pip install numpy scipy matplotlib
