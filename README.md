# Python Raytrace
A Python implementation of [Ray Tracer Challenge book](https://pragprog.com/book/jbtracer/the-ray-tracer-challenge). This mostly follows the book although there are some slight deviations:

* There is an error in one test case where the `inverse` of a rotation is used rather than the `transpose` (cite page)
* I made the ray-casting function, `position(origin, direction)` a method of the `Ray` class so it is called as `ray.position(t)` rather than `position(ray, t)`.

