from part1 import Ray, generate_ray_set



# Solution based on this answer: https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/keq7g67/
# This was a massive fucking headache even with help. 
# I still have no idea why half my math I did for this doesn't work



def get_intersection_2D(self: Ray, other: Ray, dx, dy) -> tuple[int, int]: 
    denom = ((self.dir.y -dy) * (other.dir.x -dx)) - ((self.dir.x -dx) * (other.dir.y - dy))
    if denom == 0: return None

    p1 = ((self.dir.x -dx) * (other.dir.x -dx)) * (other.origin.y - self.origin.y)
    p2 = (self.dir.y -dy) * (other.dir.x -dx) * self.origin.x
    p3 = (self.dir.x -dx) * (other.dir.y - dy) * other.origin.x

    x = (p1 + p2 - p3) / denom

    #if not (lb <= x <= ub): return False

    if (self.dir.x - dx) == 0 or (other.dir.x - dx) == 0:
        return None

    y = ((self.dir.y - dy) / (self.dir.x - dx)) * (x - self.origin.x) + self.origin.y

    #if not (lb <= y <= ub): return False

    if (x - self.origin.x) // (self.dir.x - dx) < 0: return False
    if (x - other.origin.x) // (other.dir.x - dx) < 0: return False

    return (x, y)


#TODO: Figure out what the fuck I need to do to solve this


def find_xy(s: list[Ray]) -> tuple[int, int, int, int]:
    extreme = 1000
    bounds = range(-extreme, extreme)

    for x in bounds:
        for y in bounds:

            success = True
            pos = None
            for i in range(len(s) - 1):

                new = get_intersection_2D(s[i], s[i+1], x, y)
                #print(new)

                if new == False:
                    success = False
                    break
                elif new == None:
                    pass
                elif pos == None:
                    pos = new
                elif new != pos:
                    success = False
                    break
            
            if success: 
                #print(new)
                #print(pos)
                return (x, y, pos[0], pos[1])



def main():
    s = list(generate_ray_set("input.txt"))

    vx, vy, x, y = find_xy(s)

    print(x, y)
    print(vx, vy)

    r_1 = s[0]
    r_2 = s[1]

    t_1 = (x - r_1.origin.x) // (r_1.dir.x - vx)
    t_2 = (x - r_2.origin.x) // (r_2.dir.x - vx)

    vz = (r_2.origin.z - r_1.origin.z)-(r_1.dir.z*t_1)+(r_2.dir.z*t_2)
    vz = vz // (t_2 - t_1)

    z = r_1.origin.z + ((r_1.dir.z - vz) * t_1)

    print(vz, z)

    print(x + y + z)

    # This took me an entire year to complete. I feel like a fucking god.


if __name__ == "__main__":
    main()





# 346929738756520, 180308062329517, 348158644025623 @ 6, -5, -22
# 254810664927620, 353739895010289, 244141919277765 @ -144, 403, -76

# pos(t) = (dir * t) + org
# 
# unknown:
#   pos org, pos dir
#
# p0 + t[i]*v0 == p[i] + t[i]*v[i]
# p0 - p[i] + t[i]*v0 - t[i]*v[i] = 0
# (p0 - p[i]) x t[i](v0 - v[i]) = 0

# (p0 - p[i]) x (v0 - v[i]) = 0

# (p0 - p[i]) X v0 - (p0 - p[i]) x v[i] = 0
# (p0 x v0) - (p[i] x v0) - (p0 x v[i]) + (p[i] x v[i]) = 0





# 346929738756520, 180308062329517, 348158644025623 @ 6, -5, -22
# 254810664927620, 353739895010289, 244141919277765 @ -144, 403, -76
# 295870756794909, 404627177923603, 198720163538165 @ -23, -185, 145
# 
# p0 == p[i] + t[i]*v[i] - t[i]*v0
#  p0 == p[i] + t[i](v[i] - v0)