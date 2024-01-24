/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as JulepApi from "../..";
/**
 * @example
 *     {
 *         instructions: [{
 *                 content: "string"
 *             }],
 *         defaultSettings: {
 *             temperature: 1,
 *             topP: 1
 *         }
 *     }
 */
export interface UpdateAgentRequest {
  /** About the agent */
  about?: string;
  /** List of instructions for the agent */
  instructions?: JulepApi.Instruction[];
  /** Name of the agent */
  name?: string;
  /** Name of the model that the agent is supposed to use */
  model?: string;
  /** Default model settings to start every session with */
  defaultSettings?: JulepApi.AgentDefaultSettings;
}
