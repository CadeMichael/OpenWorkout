import { Drash } from "./deps.ts";

class HomeResource extends Drash.Resource {
  public calcMax = (reps: number, weight: number) => {
    const rm = weight / (1.0278 - 0.0278 * reps);
    return rm;
  };

  public calcRel = (reps: number, weight: number, orm: number) => {
    const maxWeight = orm * (1.0278 - 0.0278 * reps);
    const ai = weight / orm;
    const ri = ai / (maxWeight / orm);
    return Math.round(ri * 100);
  };

  public paths = ["/:weight/:reps/:orm?"];

  public GET(request: Drash.Request, response: Drash.Response): void {
    const weight = request.pathParam("weight");
    const reps = request.pathParam("reps");
    const orm = request.pathParam("orm");

    if (weight && reps) {
      const weightInt = parseInt(weight);
      const repsInt = parseInt(reps);
      if (orm) {
        const ormInt = parseInt(orm);
        const ri = this.calcRel(repsInt, weightInt, ormInt);
        return response.json({ relIntensity: ri });
      } else {
        const oneRepMax = Math.round(this.calcMax(repsInt, weightInt));
        return response.json({ oneRepMax: oneRepMax });
      }
    }
  }
}

const server = new Drash.Server({
  hostname: "localhost",
  port: 1447,
  protocol: "http",
  resources: [
    HomeResource,
  ],
});

server.run();

console.log(`sever running at ${server.address}.`);
